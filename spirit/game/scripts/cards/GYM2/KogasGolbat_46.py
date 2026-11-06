from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.attributes import SpecialConditions


card = PokemonCardDef(
    guid="2ffc9bd2-ead4-5411-89c1-1dad8b73e7b7",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasGolbat.Name",
    display_name="Koga's Golbat",
    searchable_by=["Koga's Golbat", "Stage 1", "KogasGolbat"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.KogasZubat.Name",
    family_id=41,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Sonic Scream",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)
