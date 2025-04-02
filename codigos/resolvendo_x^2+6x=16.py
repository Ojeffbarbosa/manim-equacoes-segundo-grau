"""
Copyright (c) Jefferson 2024-2025. 
Demonstração visual da solução da equação quadrática x² + 6x = 16 usando o método de completar quadrados.
"""

from manim import *
import copy
import numpy as np

# Definindo cores para reutilização no código
COR_A = YELLOW       
COR_B = BLUE         
COR_C = GREEN        
COR_DESTAQUE = RED   
COR_QUADRADO1 = BLUE  
COR_RETANGULO = YELLOW   
COR_QUADRADO2 = GREEN   
COR_FUNDO = BLACK       
COR_TEXTO = BLACK       

class VideoSequencial(Scene):
    def construct(self):
        # Configuração personalizada para definir o fundo
        config.background_color = COR_FUNDO
        
        # ==================== PARTE 1: Apresentação da Equação ====================
        # Título da animação
        titulo = Text('Resolvendo x² + 6x = 16').scale(0.8).to_edge(UP)

        # Criando a equação a ser resolvida
        equacao1 = MathTex("x^2 + 6x = 16")
        
        # Criando as legendas explicativas para cada passo
        legenda1 = Text("Equação quadrática", font_size=24).to_edge(DOWN, buff=0.5)
        legenda_transicao = Text("Vamos visualizar esta equação geometricamente", font_size=28, color=YELLOW).to_edge(DOWN, buff=0.5)

        # Animações para mostrar a equação
        self.play(FadeIn(titulo))
        self.wait(1)
        self.play(
            Write(equacao1),
            FadeIn(legenda1)
        )
        self.wait(2)
        
        # Transição para a próxima parte (representação geométrica)
        self.play(
            FadeOut(titulo),
            ReplacementTransform(legenda1, legenda_transicao)
        )
        self.wait(1)
        self.play(equacao1.animate.to_edge(UP))
        self.wait(1)
        self.play(FadeOut(legenda_transicao))
        self.wait(1)
        
        # ==================== PARTE 2: Representação Geométrica Inicial ====================
        # Criando o quadrado que representa x²
        quadrado1 = Square().set_fill(COR_QUADRADO1, opacity=1).set_stroke(WHITE, width=3.5, opacity=1).move_to((-3, 0, 0))
        mais = MathTex("+").next_to(quadrado1, RIGHT, buff=0.5)
        
        # Braços e textos para indicar as dimensões do quadrado
        b11 = Brace(quadrado1, LEFT)  # Braço lateral
        b12 = Brace(quadrado1, DOWN)  # Braço inferior
        t11 = MathTex("x").next_to(b11, LEFT)  # Texto para dimensão lateral
        t12 = MathTex("x").next_to(b12, DOWN)  # Texto para dimensão inferior
        
        # Criando os retângulos que representam 6x
        retangulo1 = Rectangle(width=0.7).set_fill(COR_RETANGULO, opacity=1).set_stroke(WHITE, width=3.5, opacity=1).next_to(mais, RIGHT, buff=0.5)
        retangulo2 = Rectangle(width=0.7).set_fill(COR_RETANGULO, opacity=1).set_stroke(WHITE, width=3.5, opacity=1).next_to(retangulo1, RIGHT, buff=0)
        
        # Braços e textos para indicar as dimensões dos retângulos
        b21 = Brace(retangulo2, RIGHT)  # Braço lateral
        b22 = Brace(VGroup(retangulo1, retangulo2), DOWN)  # Braço inferior para ambos retângulos
        t21 = MathTex("x").next_to(b21, RIGHT)  # Texto para dimensão lateral
        t22 = MathTex("6").next_to(b22, DOWN)  # Texto para dimensão inferior
        
        # Criando o sinal de igualdade e a figura que representa 16
        igual = MathTex("=").next_to(retangulo2, RIGHT, buff=0.5)
        quadrado2 = Square(side_length=np.sqrt(6.3)).set_fill(COR_QUADRADO2, opacity=1).set_stroke(WHITE, width=3.5, opacity=1).next_to(igual, RIGHT, buff=0.5)
        
        # Textos que mostram o valor algébrico de cada forma
        x2 = MathTex("x^2").move_to(quadrado1).set_z_index(1000)  # Texto dentro do quadrado1
        seisX = MathTex("6x").move_to(VGroup(retangulo1, retangulo2)).set_z_index(1000)  # Texto nos retângulos
        dezesseis = MathTex("16").set_color(COR_TEXTO).move_to(quadrado2).set_z_index(1000)  # Texto no quadrado2
        
        # Animações para construir a representação geométrica
        self.wait(1)
        self.play(ReplacementTransform(copy.deepcopy(equacao1[0][0:2]), x2))  # Transforma parte da equação em x²
        self.wait(1)
        self.play(FadeIn(quadrado1), x2.animate.set_color(COR_TEXTO))
        self.wait(1)
        self.play(Write(VGroup(b11, b12, t11, t12)))  # Adiciona dimensões ao quadrado
        self.wait(1)
        self.play(Write(mais), ReplacementTransform(copy.deepcopy(equacao1[0][2:5]), seisX))  # Adiciona o sinal + e transforma parte da equação
        self.wait(1)
        self.play(FadeIn(retangulo1, retangulo2), seisX.animate.set_color(COR_TEXTO))
        self.wait(1)
        self.play(Write(VGroup(b21, b22, t21, t22)))  # Adiciona dimensões aos retângulos
        self.wait(1)
        self.play(
            FadeOut(b21, t21),
            ReplacementTransform(copy.deepcopy(equacao1[0][6:8]), quadrado2),
            Write(igual),
            FadeIn(dezesseis)
        )
        self.wait(1)
        
        # Limpeza parcial para a próxima parte
        #self.play(FadeOut(equacao1))
        #self.wait(1)
        
        # ==================== PARTE 3: Reorganização Geométrica ====================
        # Aproxima os retângulos
        self.wait(1)
        self.play(retangulo2.animate.next_to(retangulo1, RIGHT, buff=0.1), FadeOut(b22, t22))
        self.wait(1)
        
        # Divide visualmente o retângulo em duas partes iguais (3 cada)
        b31 = Brace(retangulo1, DOWN)
        b32 = Brace(retangulo2, DOWN)
        t31 = MathTex("3").next_to(b31, DOWN)
        t32 = MathTex("3").next_to(b32, DOWN)
        self.play(Write(VGroup(b31, b32, t31, t32)))
        self.wait(1)
        
        # Remove elementos desnecessários e prepara a reorganização
        self.play(FadeOut(b32, t32, mais, seisX))

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
        t4 = MathTex("3").next_to(b4, LEFT)
        self.play(Write(VGroup(b4, t4)))
        self.wait(1)
        
        # Reposiciona os elementos à direita (igualdade e quadrado2)
        self.play(VGroup(igual, quadrado2, dezesseis).animate.next_to(VGroup(retangulo1, retangulo2), RIGHT, buff=0.5))
        self.play(VGroup(igual, quadrado2, dezesseis, quadrado1, retangulo1, retangulo2, b11, b12, t11, t12, b31, t31, b4, t4, x2).animate.shift(UP*0.3))
        self.wait(1)
        
        # ==================== PARTE 4: Completando o Quadrado ====================
        # Adiciona novamente a equação para referência
        equacao4 = MathTex("x^2 + 6x = 16").to_edge(UP)
        self.play(FadeIn(equacao4))
        
        # Adiciona textos explicativos nos retângulos
        tt1 = MathTex("3x").set_color(COR_TEXTO).rotate(3*PI/2).move_to(retangulo1)
        tt2 = MathTex("3x").set_color(COR_TEXTO).move_to(retangulo2)

        quadrado_amarelo1 = VGroup(tt1, retangulo1)
        quadrado_amarelo2 = VGroup(tt2, retangulo2)

        # Cria o quadrado complementar para completar o quadrado perfeito
        quadrado5 = Square(side_length=.7).next_to(retangulo1, UP, buff=0).set_fill(COR_DESTAQUE, opacity=1).set_stroke(WHITE, width=3.5, opacity=1)
        texto_quadrado5 = MathTex("9").set_color(COR_TEXTO).move_to(quadrado5).set_z_index(1000)
        
        # Animações para explicar os retângulos e suas dimensões
        self.play(Write(tt2))
        self.wait(1)
        self.play(Write(tt1))

        self.play(Indicate(quadrado1))
        self.wait(1)

        # Criando expressões para a equação expandida na parte inferior
        texto_x2 = MathTex("x^2").scale(1).to_edge(DOWN, buff=1.2).shift(LEFT*3)
        texto_mais1 = MathTex("+").scale(1).next_to(texto_x2, RIGHT, buff=0.3)
        texto_3x1 = MathTex("3x").scale(1).next_to(texto_mais1, RIGHT, buff=0.3)
        texto_mais2 = MathTex("+").scale(1).next_to(texto_3x1, RIGHT, buff=0.3)
        texto_3x2 = MathTex("3x").scale(1).next_to(texto_mais2, RIGHT, buff=0.3)
        texto_mais3 = MathTex("+").scale(1).next_to(texto_3x2, RIGHT, buff=0.3)
        texto_9 = MathTex("9").scale(1).next_to(texto_mais3, RIGHT, buff=0.3)
        texto_igual = MathTex("=").scale(1).next_to(texto_9, RIGHT, buff=0.3)
        texto_16 = MathTex("16").scale(1).next_to(texto_igual, RIGHT, buff=0.3)
        texto_mais4 = MathTex("+").scale(1).next_to(texto_16, RIGHT, buff=0.3)
        texto_9_2 = MathTex("9").scale(1).next_to(texto_mais4, RIGHT, buff=0.3)
        
        # Animações para construir a expressão algébrica a partir da representação geométrica
        texto_x2_final = texto_x2.copy().set_color(BLUE)
        self.remove(texto_x2)
        self.play(TransformFromCopy(quadrado1, texto_x2_final))
        self.wait(0.5)

        self.play(Write(texto_mais1))

        texto_3x1_final = texto_3x1.copy().set_color(YELLOW)
        self.remove(texto_3x1)
        self.play(TransformFromCopy(retangulo1, texto_3x1_final))
        self.wait(0.5)

        self.play(Write(texto_mais2))

        texto_3x2_final = texto_3x2.copy().set_color(YELLOW)
        self.remove(texto_3x2)
        self.play(TransformFromCopy(retangulo2, texto_3x2_final))
        self.wait(0.5)
        
        self.play(Write(texto_igual))

        texto_16_final = texto_16.copy().set_color(GREEN)
        self.remove(texto_16)
        self.play(TransformFromCopy(quadrado2, texto_16_final))
        self.wait(0.5)

        # Mostra o espaço vazio com uma interrogação (espaço que falta para completar o quadrado)
        interrogacao = Tex("?").scale(0.9).next_to(retangulo1, UP, buff=0.25).set_fill(WHITE, opacity=1).set_stroke(opacity=0)
        quadrado_interrogacao = Square(side_length=.7).next_to(retangulo1, UP, buff=0).set_fill(BLACK, opacity=1).set_stroke(WHITE, width=3.5, opacity=1)
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
        texto_9_final = texto_9.copy().set_color(RED)
        self.remove(texto_9)
        self.play(TransformFromCopy(quadrado5, texto_9_final))
        self.wait(0.5)

        # Adiciona o sinal de + à direita do quadrado constante
        texto_mais_direito = MathTex("+").scale(1).next_to(quadrado2, RIGHT, buff=0.5)
        self.play(Write(texto_mais_direito))
        self.wait(1)
        
        # Adiciona o quadrado complementar do lado direito da equação
        quadrado_direito = Square(side_length=.7).next_to(texto_mais_direito, RIGHT, buff=0.5).set_fill(COR_DESTAQUE, opacity=1).set_stroke(WHITE, width=3.5, opacity=1)
        texto_quadrado_direito = MathTex("9").set_color(COR_TEXTO).move_to(quadrado_direito).set_z_index(1000)
        self.play(Create(quadrado_direito))
        self.play(Write(texto_quadrado_direito)) 
        self.wait(1)

        self.play(Write(texto_mais4))
        self.wait(0.5)

        texto_9_2_final = texto_9_2.copy().set_color(RED)
        self.remove(texto_9_2)
        self.play(TransformFromCopy(quadrado_direito, texto_9_2_final))
        self.wait(1)

        # ==================== PARTE 5: Quadrado Perfeito ====================
        # Cria quadrado perfeito que engloba todas as peças
        tamanho_lado = quadrado1.width + quadrado5.width  # x + 3

        # Cria um quadrado maior que abrange o quadrado original e os retângulos
        quadrado_perfeito = Square(side_length=tamanho_lado).set_fill(COR_QUADRADO1, opacity=1).set_stroke(WHITE, width=2, opacity=1).move_to(quadrado1.get_center() + 
                                np.array([quadrado5.width/2, quadrado5.height/2, 0]))
        quadrado_perfeito.set_z_index(10000)
        
        self.play(
            FadeOut(x2, tt1, tt2, texto_quadrado5)              
        )

        # Destaca as formas que compõem o quadrado perfeito
        vgroupquadrado = VGroup(quadrado1, quadrado5, retangulo1, retangulo2)
        self.play(Indicate(vgroupquadrado, color=YELLOW))
        self.play(Create(quadrado_perfeito))
        self.wait(1)

        # Destaca as dimensões para mostrar que é (x + 3)²
        self.play(Indicate(VGroup(t12, t31)))
        self.play(Indicate(VGroup(t11, t4)))
        textoquadradoperfeito = MathTex("(x+3)^2").scale(0.6).set_color(COR_TEXTO).move_to(quadrado_perfeito).set_z_index(10001)
        self.play(Write(textoquadradoperfeito))

        # Cria grupo com toda a expressão expandida
        expressao_quadrado_completo = VGroup(
            texto_x2_final,
            texto_mais1, 
            texto_3x1_final, 
            texto_mais2, 
            texto_3x2_final, 
            texto_mais3, 
            texto_9_final
        )
        
        # Transforma a expressão expandida na expressão fatorada
        algebraquadradoperfeito = MathTex("(x+3)^2").set_color(BLUE).next_to(texto_igual, LEFT, buff=0.3).set_z_index(1002)
        self.play(ReplacementTransform(expressao_quadrado_completo, algebraquadradoperfeito))
        self.wait(1)

        # Agrupa as expressões da parte inferior da equação
        expressao_inferior = VGroup(
            algebraquadradoperfeito,
            texto_igual,
            texto_16_final,
            texto_mais4,
            texto_9_2_final
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
            texto_quadrado_direito,
            texto_mais_direito,
            dezesseis,
            
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
            "(x+3)^2", "=", "16", "+", "9"
        ).scale(0.9)
        legenda = Text("Vamos somar o lado direito", font_size=24).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(expressao_inferior, expressao_completa), FadeIn(legenda))
        self.wait(2)
        
        # Simplifica o lado direito
        expressao2 = MathTex(
            "(x+3)^2", "=", "25"
        ).scale(0.9)
        legenda2 = Text("Iremos aplicar a raiz quadrada em ambos os lados", font_size=24).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(expressao_completa, expressao2), ReplacementTransform(legenda, legenda2))
        self.wait(2)

        # Extrai a raiz quadrada de ambos os lados
        expressao3 = MathTex(
            "x+3", "=", "\\pm 5"
        ).scale(0.9)
        legenda3 = Text("Agora, isolamos o x", font_size=24).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(expressao2, expressao3), ReplacementTransform(legenda2, legenda3))
        self.wait(2)

        # Isola o x
        expressao4 = MathTex(
            "x", "=", "-3 \\pm 5"
        ).scale(0.9)
        legenda4 = Text("Temos duas soluções", font_size=24).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(expressao3, expressao4), ReplacementTransform(legenda3, legenda4))
        self.wait(2)

        # Mostra o cálculo explícito
        expressao_calculo = MathTex(
            "x = -3 + 5 \\text{ ou } x = -3 - 5"
        ).scale(0.9)
        legenda_calculo = Text("Calculando as duas possibilidades", font_size=24).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(expressao4, expressao_calculo), ReplacementTransform(legenda4, legenda_calculo))
        self.wait(2)

        # Mostra as duas soluções
        expressao5 = MathTex(
            "x = 2 \\text{ ou } x = -8"
        ).scale(0.9)
        legenda5 = Text("Estas são as soluções da equação!", font_size=24).to_edge(DOWN, buff=0.5)
        self.play(ReplacementTransform(expressao_calculo, expressao5), ReplacementTransform(legenda_calculo, legenda5))
        self.wait(2)
        
        # Destaque final para as soluções
        legenda_final = Text("Estas são as soluções da equação!", font_size=28, color=YELLOW).to_edge(DOWN, buff=0.5)
        self.play(
            expressao5.animate.set_color(YELLOW).scale(1.2),
            ReplacementTransform(legenda5, legenda_final)
        )

        # Cria retângulo de destaque em torno da solução final
        retangulo_final = SurroundingRectangle(expressao5, color=YELLOW, buff=0.2)
        self.play(Create(retangulo_final))
        self.wait(5)
