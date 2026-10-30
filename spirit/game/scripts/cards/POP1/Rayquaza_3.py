"""STUB: effect not implemented — do not guess mechanics.
Rayquaza (POP1 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import fly_flip_protect
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="83c2ffbb-ff54-598b-b033-c5110327cd8c",
    key="POP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza",
    searchable_by=["Rayquaza", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="POP1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    family_id=384,
    abilities=[
        Attack(
            title="Fly",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, prevent all effects of an attack, including damage, done to Rayquaza during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=fly_flip_protect(),
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
    ],
)