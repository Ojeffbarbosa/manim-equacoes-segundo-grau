"""
Copyright (c) Jefferson 2024-2025. 
Demonstração visual da dedução da fórmula quadrática usando Manim.
"""

from manim import *
import copy
import numpy as np

# Definindo cores para reutilização no código
COR_A = ORANGE       # Cor utilizada para o primeiro quadrado/retângulos
COR_C = '#00FF7E'    # Cor verde utilizada para o segundo quadrado  
COR_DESTAQUE = RED   # Cor para destacar elementos
COR_QUADRADO1 = '#00FFFF'  # Cor ciano para o quadrado principal (x²)
COR_RETANGULO = ORANGE     # Cor laranja para os retângulos (bx/a)
COR_QUADRADO2 = COR_C      # Cor verde para o quadrado constante (-c/a)
COR_FUNDO = BLACK     # Cor de fundo da cena
COR_TEXTO = BLACK     # Cor do texto dentro das formas
LEMOM = '#FDFF52'     # Cor amarela para o quadrado complementar (b²/4a²)

class VideoSequencial(Scene):
    def construct(self):
        # Configuração personalizada para definir o fundo
        config.background_color = COR_FUNDO
        
        # ==================== PARTE 1: Manipulação Algébrica Inicial ====================
        # Título da animação
        titulo = Text('A Fórmula quadrática').scale(1).to_edge(UP)

        # Criando as equações para a demonstração algébrica
        equacao1 = MathTex("ax^2 + bx+ c= 0")  # Equação padrão
        equacao3 = MathTex("x^2 + \\frac{b}{a}x+ \\frac{c}{a}= 0")  # Equação dividida por 'a'
        equacao2 = MathTex("x^2 + \\frac{b}{a}x= - \\frac{c}{a}")  # Equação com termo constante isolado
        
        # Criando as legendas explicativas para cada passo
        legenda1 = Text("Partimos da equação quadrática na sua forma padrão", font_size=24).to_edge(DOWN, buff=0.5)
        legenda2 = Text("Agora vamos dividir toda a equação por 'a'", font_size=24).to_edge(DOWN, buff=0.5)
        legenda3 = Text("Em seguida, isolamos o termo constante à direita", font_size=24).to_edge(DOWN, buff=0.5)
        legenda_transicao = Text("Vamos visualizar esta equação geometricamente", font_size=28, color=YELLOW).to_edge(DOWN, buff=0.5)

        # Animações para mostrar a manipulação algébrica
        self.play(FadeIn(titulo))
        self.wait(2)  
        self.play(
            Write(equacao1),
            FadeIn(legenda1)
        )
        self.wait(3)  
        self.play(
            (ReplacementTransform(legenda1, legenda2))
        )
        self.wait(3) 
        self.play(ReplacementTransform(equacao1, equacao3))
        self.wait(3)  
        self.play(
            ReplacementTransform(legenda2, legenda3)
        )
        self.wait(3)  
        self.play(
            ReplacementTransform(equacao3, equacao2),
        )
        
        # Transição para a próxima parte (representação geométrica)
        self.play(
            FadeOut(titulo),
            ReplacementTransform(legenda3, legenda_transicao)
        )
        self.wait(2)  
        self.play(equacao2.animate.to_edge(UP))
        self.wait(2)  
        self.play(FadeOut(legenda_transicao))
        self.wait(1)  
        
        # ==================== PARTE 2: Representação Geométrica Inicial ====================
        # Criando o quadrado que representa x²
        quadrado1 = Square().set_fill(COR_QUADRADO1, opacity=1).set_stroke(width=3.5,opacity=1).move_to((-3, 0, 0))
        mais = MathTex("+").next_to(quadrado1, RIGHT, buff=0.5)
        
        # Braços e textos para indicar as dimensões do quadrado
        b11 = Brace(quadrado1, LEFT)  # Braço lateral
        b12 = Brace(quadrado1, DOWN)  # Braço inferior
        t11 = MathTex("x").next_to(b11, LEFT)  # Texto para dimensão lateral
        t12 = MathTex("x").next_to(b12, DOWN)  # Texto para dimensão inferior
        
        # Criando os retângulos que representam (b/a)x
        retangulo1 = Rectangle(width=1).set_fill(COR_RETANGULO, opacity=1).set_stroke(width=3.5,opacity=1).next_to(mais, RIGHT, buff=0.5)
        retangulo2 = Rectangle(width=1).set_fill(COR_RETANGULO, opacity=1).set_stroke(width=3.5,opacity=1).next_to(retangulo1, RIGHT, buff=0)
        
        # Braços e textos para indicar as dimensões dos retângulos
        b21 = Brace(retangulo2, RIGHT)  # Braço lateral
        b22 = Brace(VGroup(retangulo1, retangulo2), DOWN)  # Braço inferior para ambos retângulos
        t21 = MathTex("x").next_to(b21, RIGHT)  # Texto para dimensão lateral
        t22 = MathTex("\\frac{b}{a}").next_to(b22, DOWN)  # Texto para dimensão inferior
        
        # Criando o sinal de igualdade e a figura que representa -c/a
        igual = MathTex("=").next_to(retangulo2, RIGHT, buff=0.5)
        quadrado2 = Square(side_length=np.sqrt(6.4)).set_fill(COR_QUADRADO2, opacity=1).set_stroke(width=3.5,opacity=1).next_to(igual, RIGHT, buff=0.5)
        
        # Textos que mostram o valor algébrico de cada forma
        x2 = MathTex("x^2").move_to(quadrado1).set_z_index(1000)  # Texto dentro do quadrado1
        quatrox = MathTex("\\frac{b}{a}x").move_to(VGroup(retangulo1, retangulo2)).set_z_index(1000)  # Texto nos retângulos
        cinco = MathTex("-\\frac{c}{a}").set_color(COR_TEXTO).move_to(quadrado2).set_z_index(1000)  # Texto no quadrado2
        
        # Animações para construir a representação geométrica
        self.wait(1)
        self.play(ReplacementTransform(copy.deepcopy(equacao2[0][0:2]), x2))  # Transforma parte da equação em x²
        self.wait(1)
        self.play(FadeIn(quadrado1), x2.animate.set_color(COR_TEXTO))
        self.wait(1)
        self.play(Write(VGroup(b11, b12, t11, t12)))  # Adiciona dimensões ao quadrado
        self.wait(1)
        self.play(Write(mais), ReplacementTransform(copy.deepcopy(equacao2[0][4:6]), quatrox))  # Adiciona o sinal + e transforma parte da equação
        self.wait(1)
        self.play(FadeIn(retangulo1, retangulo2), quatrox.animate.set_color(COR_TEXTO))
        self.wait(1)
        self.play(Write(VGroup(b21, b22, t21, t22)))  # Adiciona dimensões aos retângulos
        self.wait(1)
        self.play(
            FadeOut(b21, t21),
            ReplacementTransform(copy.deepcopy(equacao2[0][6]), quadrado2),
            Write(igual),
            FadeIn(cinco)
        )
        self.wait(1)
        
        # Limpeza parcial para a próxima parte
        self.play(FadeOut(equacao2))
        self.wait(1)
        
        # ==================== PARTE 3: Reorganização Geométrica ====================
        # Aproxima os retângulos
        self.wait(1)
        self.play(retangulo2.animate.next_to(retangulo1, RIGHT, buff=0.1), FadeOut(b22, t22))
        self.wait(1)
        
        # Divide visualmente o retângulo em duas partes iguais (b/2a cada)
        b31 = Brace(retangulo1, DOWN)
        b32 = Brace(retangulo2, DOWN)
        t31 = MathTex("\\frac{b}{2a}").scale(0.8).next_to(b31, DOWN)
        t32 = MathTex("\\frac{b}{2a}").scale(0.8).next_to(b32, DOWN)
        self.play(Write(VGroup(b31, b32, t31, t32)))
        self.wait(1)
        
        # Remove elementos desnecessários e prepara a reorganização
        self.play(FadeOut(b32, t32, mais, quatrox))

        # Configuração para manter o braço alinhado durante a animação
        y_pos = b12.get_center()[1]
        b31.set_y(y_pos)
        t31.next_to(b31, DOWN)

        # Adiciona updaters para manter o braço e texto atualizados durante a animação
        def update_brace(b):
            b.become(Brace(retangulo1, DOWN))
            b.set_y(y_pos)  # Mantém o alinhamento Y com b12
            return b

        def update_text(t):
            t.next_to(b31, DOWN)
            return t

        b31.add_updater(update_brace)
        t31.add_updater(update_text)

        # Reorganiza os retângulos para formar um quadrado perfeito
        self.play(
            retangulo1.animate.next_to(quadrado1, RIGHT, buff=0),  # Move o primeiro retângulo para a direita do quadrado
            Rotate(retangulo2, angle=PI/2, rate_func=linear)  # Rotaciona o segundo retângulo 90 graus
        )

        # Remove os updaters após completar o movimento
        b31.clear_updaters()
        t31.clear_updaters()

        # Posiciona o retângulo rotacionado acima do quadrado
        self.play(retangulo2.animate.next_to(quadrado1, UP, buff=0))
        
        # Adiciona braço e texto para o retângulo rotacionado
        b4 = Brace(retangulo2, LEFT)
        t4 = MathTex("\\frac{b}{2a}").scale(0.8).next_to(b4, LEFT)
        self.play(Write(VGroup(b4, t4)))
        self.wait(1)
        
        # Reposiciona os elementos à direita (igualdade e quadrado2)
        self.play(VGroup(igual, quadrado2, cinco).animate.next_to(VGroup(retangulo1, retangulo2), RIGHT, buff=0.5))
        self.play(VGroup(igual, quadrado2, cinco, quadrado1, retangulo1, retangulo2, b11, b12, t11, t12, b31, t31, b4, t4, x2).animate.shift(UP*1))
        self.wait(1)
        
        # ==================== PARTE 4: Completando o Quadrado ====================
        # Nota: equacao2 aqui deveria ser renomeada pois já foi usada antes
        equacao2 = MathTex("x^2 + 6x = 16").to_edge(UP).shift(LEFT * 1)  # Exemplo específico da equação
        
        # Adiciona textos explicativos nos retângulos
        tt1 = MathTex("\\frac{b}{2a}x").scale(0.8).set_color(COR_TEXTO).rotate(3*PI/2).move_to(retangulo1).set_z_index(1001)
        tt2 = MathTex("\\frac{b}{2a}x").scale(0.8).set_color(COR_TEXTO).move_to(retangulo2).set_z_index(1001)

        # Cria o quadrado complementar para completar o quadrado perfeito
        quadrado5 = Square(side_length=1).next_to(retangulo1, UP, buff=0).set_fill(LEMOM, opacity=1).set_stroke(width=3.5,opacity=1)
        texto_quadrado5 = MathTex("\\left(\\frac{b}{2a}\\right)^2").scale(0.6).set_color(COR_TEXTO).move_to(quadrado5).set_z_index(1000)
        
        # Animações para explicar os retângulos e suas dimensões
        self.play(Write(tt2))
        self.wait(1)
        self.play(Write(tt1))

        self.play(Indicate(quadrado1))
        self.wait(1)

        # Criando expressões para a equação expandida na parte inferior
        texto_x2 = MathTex("x^2").scale(0.9).to_edge(DOWN, buff=1.2).shift(LEFT*4)
        texto_mais1 = MathTex("+").scale(0.9).next_to(texto_x2, RIGHT, buff=0.3)
        texto_3x1 = MathTex("\\frac{b}{2a}x").scale(0.9).next_to(texto_mais1, RIGHT, buff=0.3)
        texto_mais2 = MathTex("+").scale(0.9).next_to(texto_3x1, RIGHT, buff=0.3)
        texto_3x2 = MathTex("\\frac{b}{2a}x").scale(0.9).next_to(texto_mais2, RIGHT, buff=0.3)
        texto_mais3 = MathTex("+").scale(0.9).next_to(texto_3x2, RIGHT, buff=0.3)
        texto_9 = MathTex("\\left(\\frac{b}{2a}\\right)^2").scale(0.9).next_to(texto_mais3, RIGHT, buff=0.3)
        texto_igual = MathTex("=").scale(0.9).next_to(texto_9, RIGHT, buff=0.3)
        texto_16 = MathTex("-\\frac{c}{a}").scale(0.9).next_to(texto_igual, RIGHT, buff=0.3)
        texto_mais4 = MathTex("+").scale(0.9).next_to(texto_16, RIGHT, buff=0.3)
        texto_9_2 = MathTex("\\left(\\frac{b}{2a}\\right)^2").scale(0.9).next_to(texto_mais4, RIGHT, buff=0.3)
        
        # Animações para construir a expressão algébrica a partir da representação geométrica
        texto_x2_final = texto_x2.copy().set_color(COR_QUADRADO1)
        self.remove(texto_x2)
        self.play(TransformFromCopy(quadrado1, texto_x2_final))
        self.wait(0.5)

        self.play(Write(texto_mais1))

        texto_3x1_final = texto_3x1.copy().set_color(ORANGE)
        self.remove(texto_3x1)
        self.play(TransformFromCopy(retangulo1, texto_3x1_final))
        self.wait(0.5)

        self.play(Write(texto_mais2))

        texto_3x2_final = texto_3x2.copy().set_color(ORANGE)
        self.remove(texto_3x2)
        self.play(TransformFromCopy(retangulo2, texto_3x2_final))
        self.wait(0.5)
        
        self.play(Write(texto_igual))

        texto_16 = texto_16.copy().set_color(COR_C)
        self.remove(texto_16)
        self.play(TransformFromCopy(quadrado2, texto_16))
        self.wait(0.5)

        # Mostra o espaço vazio com uma interrogação (espaço que falta para completar o quadrado)
        interrogacao = Tex("?").scale(1).next_to(retangulo1, UP, buff=0.25).set_fill(WHITE, opacity=1).set_stroke(opacity=0)
        quadrado_interrogacao = Square(side_length=1).next_to(retangulo1, UP, buff=0).set_fill(BLACK, opacity=1).set_stroke(width=3, opacity=1)
        inter = VGroup(quadrado_interrogacao, interrogacao)

        self.play(Indicate(inter, color=PINK))
        self.wait(0.5)
        self.play(FadeOut(inter))
        self.wait(1)

        # Adiciona o quadrado complementar no espaço que faltava
        self.play(Create(quadrado5))
        self.play(Write(texto_quadrado5)) 
        self.wait(1)
        self.play(Write(texto_mais3))
        texto_9 = texto_9.copy().set_color(LEMOM)
        self.remove(texto_9)
        self.play(TransformFromCopy(quadrado5, texto_9))
        self.wait(0.5)

        # Adiciona o sinal de + à direita do quadrado constante
        texto_mais_direito = MathTex("+").scale(0.9).next_to(quadrado2, RIGHT, buff=0.5)
        self.play(Write(texto_mais_direito))
        self.wait(1)
        
        # Adiciona o quadrado complementar do lado direito da equação
        quadrado_direito = Square(side_length=1).next_to(texto_mais_direito, RIGHT, buff=0.5).set_fill(LEMOM, opacity=1).set_stroke(width=3.5,opacity=1)
        texto_quadrado_direito = MathTex("\\left(\\frac{b}{2a}\\right)^2").scale(0.6).set_color(COR_TEXTO).move_to(quadrado_direito).set_z_index(1000)
        self.play(Create(quadrado_direito))
        self.play(Write(texto_quadrado_direito)) 
        self.wait(1)

        self.play(Write(texto_mais4))
        self.wait(0.5)

        texto_9_2 = texto_9_2.copy().set_color(LEMOM)
        self.remove(texto_9_2)
        self.play(TransformFromCopy(quadrado_direito, texto_9_2))
        self.wait(1)

        # ==================== PARTE 5: Quadrado Perfeito ====================
        # Cria quadrado perfeito que engloba todas as peças
        tamanho_lado = quadrado1.width + quadrado5.width  # x + b/2a

        MAGENTA='#EC008C'

        # Cria um quadrado maior que abrange o quadrado original e os retângulos
        quadrado_perfeito = Square(side_length=tamanho_lado).set_fill(MAGENTA, opacity=1).set_stroke(width=3.5,opacity=1).move_to(quadrado1.get_center() + 
                                np.array([quadrado5.width/2, quadrado5.height/2, 0]))
        
        quadrado_perfeito.set_z_index(1001)
        self.play(
            FadeOut(x2, tt1, tt2, texto_quadrado5)              
        )

        # Destaca as formas que compõem o quadrado perfeito
        vgroupquadrado = VGroup(quadrado1, quadrado5, retangulo1, retangulo2)
        self.play(Indicate(vgroupquadrado, color=YELLOW))
        self.play(Create(quadrado_perfeito))
        self.wait(1)

        # Destaca as dimensões para mostrar que é (x + b/2a)²
        self.play(Indicate(VGroup(t12, t31)))
        self.play(Indicate(VGroup(t11, t4)))
        textoquadradoperfeito = MathTex("\\left(x+\\frac{b}{2a}\\right)^2").scale(0.6).set_color(COR_TEXTO).move_to(quadrado_perfeito).set_z_index(1002)
        self.play(Write(textoquadradoperfeito))

        # Cria grupo com toda a expressão expandida
        expressao_quadrado_completo = VGroup(
            texto_x2_final,
            texto_mais1, 
            texto_3x1_final, 
            texto_mais2, 
            texto_3x2_final, 
            texto_mais3, 
            texto_9
        )
        
        # Transforma a expressão expandida na expressão fatorada
        algebraquadradoperfeito = MathTex("\\left(x+\\frac{b}{2a}\\right)^2").set_color(MAGENTA).next_to(texto_igual, LEFT, buff=0.3).set_z_index(1002)
        self.play(ReplacementTransform(expressao_quadrado_completo, algebraquadradoperfeito))
        self.wait(1)

        # Agrupa as expressões da parte inferior da equação
        expressao_inferior = VGroup(
            algebraquadradoperfeito,
            texto_igual,
            texto_16,
            texto_mais4,
            texto_9_2
        )
        
        # Agrupa todos os elementos visuais superiores para removê-los
        elementos_superiores = VGroup(
            # Quadrado principal e seu texto
            quadrado_perfeito,
            textoquadradoperfeito,
            
            # Elementos geométricos originais
            quadrado1,
            quadrado5, 
            retangulo1, 
            retangulo2,
            
            # Elementos à direita da igualdade
            quadrado2,
            quadrado_direito,
            texto_quadrado_direito,  # Corrigido aqui
            texto_mais_direito,
            cinco,
            
            # Braços e textos de medidas
            b11, b12, t11, t12,
            b31, t31,
            b4, t4,
            
            # Símbolo de igualdade
            igual
        )

        # Remove a representação geométrica para focar na manipulação algébrica
        self.play(FadeOut(elementos_superiores))

        # ==================== PARTE 6: Dedução Algébrica Final ====================
        # Cria uma expressão unificada com o quadrado perfeito
        expressao_completa = MathTex(
            "\\left(x+\\frac{b}{2a}\\right)^2", "=", "-\\frac{c}{a}", "+", "\\left(\\frac{b}{2a}\\right)^2"
        ).scale(0.9)
        legenda = Text("Vamos aplicar a raiz quadrada em ambos os lados", font_size=24).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(expressao_inferior, expressao_completa), FadeIn(legenda))
        self.wait(3)
        
        # Extrai a raiz quadrada de ambos os lados
        expressao2 = MathTex(
            "x+\\frac{b}{2a}", "=", "\\pm\\sqrt{-\\frac{c}{a} + \\left(\\frac{b}{2a}\\right)^2}"
        ).scale(0.9)
        legenda2 = Text("Agora vamos simplificar a expressão dentro da raiz", font_size=24).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(expressao_completa, expressao2), ReplacementTransform(legenda, legenda2))
        self.wait(3)

        # Simplifica o radical
        expressao3 = MathTex(
            "x+\\frac{b}{2a}", "=", "\\pm\\sqrt{\\frac{b^2}{4a^2} - \\frac{c}{a}}"
        ).scale(0.9)
        legenda3 = Text("Vamos encontrar o denominador comum dentro da raiz", font_size=24).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(expressao2, expressao3), ReplacementTransform(legenda2, legenda3))
        self.wait(3)

        # Encontra o mínimo múltiplo comum no denominador
        expressao4 = MathTex(
            "x+\\frac{b}{2a}", "=", "\\pm\\sqrt{\\frac{b^2 - 4ac}{4a^2}}"
        ).scale(0.9)
        legenda4 = Text("Vamos extrair a raiz quadrada do denominador", font_size=24).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(expressao3, expressao4), ReplacementTransform(legenda3, legenda4))
        self.wait(3)

        # Extrai a raiz quadrada do denominador
        expressao5 = MathTex(
            "x+\\frac{b}{2a}", "=", "\\pm\\frac{\\sqrt{b^2 - 4ac}}{2a}"
        ).scale(0.9)
        legenda5 = Text("Agora vamos isolar o x para um lado da equação", font_size=24).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(expressao4, expressao5), ReplacementTransform(legenda4, legenda5))
        self.wait(3)

        # Isola o x
        expressao6 = MathTex(
            "x", "=", "-\\frac{b}{2a}", "\\pm", "\\frac{\\sqrt{b^2 - 4ac}}{2a}"
        ).scale(0.9)
        legenda6 = Text("Como os denominadores já são iguais, podemos juntar os termos em uma única fração", font_size=24).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(expressao5, expressao6), ReplacementTransform(legenda5, legenda6))
        self.wait(3)

        # Fatora o denominador comum para chegar à fórmula quadrática
        expressao7 = MathTex(
            "x", "=", "\\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}"
        ).scale(0.9)
        legenda7 = Text("E assim chegamos à fórmula resolutiva de equações quadráticas", font_size=24).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(expressao6, expressao7), ReplacementTransform(legenda6, legenda7))
        self.wait(3)
        
        # Destaque final para a fórmula
        legenda_final = Text("Esta é a famosa Fórmula!", font_size=28, color=YELLOW).to_edge(DOWN, buff=0.5)
        self.play(
            expressao7.animate.set_color(YELLOW).scale(1.2),
            ReplacementTransform(legenda7, legenda_final), 
        )

        # Cria retângulo de destaque em torno da fórmula final
        retangulo_final = SurroundingRectangle(expressao7, color=YELLOW, buff=0.2)
        self.play(Create(retangulo_final))
        self.wait(5)  # Pausa final
