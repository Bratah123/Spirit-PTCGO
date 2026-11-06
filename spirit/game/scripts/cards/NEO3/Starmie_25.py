from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import core_stream


card = PokemonCardDef(
    guid="954e9fed-a701-5f7f-8fb9-0f4a11c814e5",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Confuse Ray",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
        Attack(
            title="Core Stream",
            game_text="Choose an Energy type other than Colorless. This attack does 20 damage to each of your opponent's Pok\u00e9mon with any Energy cards of that type attached to it. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            effect=core_stream,
        ),
    ],
)
