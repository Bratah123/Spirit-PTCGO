from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import good_morning


card = PokemonCardDef(
    guid="e676b2d3-0945-51fb-9837-fae9ff43b612",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasJynx.Name",
    display_name="Sabrina's Jynx",
    searchable_by=["Sabrina's Jynx", "Basic", "SabrinasJynx"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=124,
    abilities=[
        Attack(
            title="Good Night",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Good Morning",
            game_text="If the Defending Pok\u00e9mon was Asleep, it is no longer Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=good_morning,
        ),
    ],
)
