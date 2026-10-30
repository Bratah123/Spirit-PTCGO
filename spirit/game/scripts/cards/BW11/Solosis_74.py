from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="62403b3c-973f-5682-a217-da07eaa9913b",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solosis.Name",
    display_name="Solosis",
    searchable_by=["Solosis", "Basic", "Solosis"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="BW11",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=577,
    abilities=[
        Attack(
            title="Nap",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=heal_attack(20),
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)