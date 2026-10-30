"""STUB: effect not implemented — do not guess mechanics.
Scyther (EX10 #46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import flip_agility_protect, twin_play

card = PokemonCardDef(
    guid="2c6b3f69-0416-5873-b872-76637b6ca60d",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    display_name="Scyther",
    searchable_by=["Scyther", "Basic", "Scyther"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=123,
    abilities=[
        Attack(
            title="Twin Play",
            game_text="Search your deck for up to 2 in any combination of Scyther and Scyther ex and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=twin_play("Scyther"),
        ),
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, prevent all effects of an attack, including damage, done to Scyther during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=flip_agility_protect(),
        ),
    ],
)