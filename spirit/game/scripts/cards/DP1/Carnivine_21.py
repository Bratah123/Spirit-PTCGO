"""Carnivine (POP8 #7)."""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import swallow_up_instead, wring_out_paralyze_discard


card = PokemonCardDef(
    guid="6e931c33-27d0-55eb-aaae-b63e6cad8508",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name",
    display_name="Carnivine",
    searchable_by=["Carnivine", "Basic", "Carnivine"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="DP1",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=455,
    abilities=[
        Attack(
            title="Swallow Up",
            game_text="Before doing damage, count the remaining HP of the Defending Pok\u00e9mon and Carnivine. If the Defending Pok\u00e9mon has fewer remaining HP than Carnivine's, this attack does 60 damage instead.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=swallow_up_instead(30, 60),
        ),
        Attack(
            title="Wring Out",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed and discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            effect=wring_out_paralyze_discard(),
        ),
    ],
)
