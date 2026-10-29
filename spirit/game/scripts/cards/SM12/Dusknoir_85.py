from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm4 import psych_up
from spirit.game.card_effects.sm12 import grim_marking


card = PokemonCardDef(
    guid="8d0fe204-3170-5489-b132-47778a602f47",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name",
    display_name="Dusknoir",
    searchable_by=["Dusknoir", "Stage 2", "Dusknoir"],
    subtypes=["Stage 2"],
    collector_number=85,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    family_id=355,
    abilities=[
        Ability(
            title="Grim Marking",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is Knocked Out by damage from an opponent's attack, put 4 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=grim_marking,
        ),
        Attack(
            title="Psych Up",
            game_text="During your next turn, this Pok\u00e9mon's Psych Up attack does 60 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
            effect=psych_up,
        ),
    ],
)