from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="ef2a7c7e-183e-511d-97ae-3b9eb287c19c",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    display_name="Hoothoot",
    searchable_by=["Hoothoot", "Basic", "Hoothoot"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=163,
    abilities=[
        Attack(
            title="Hypnosis",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
