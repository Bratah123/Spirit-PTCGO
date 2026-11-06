from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import switch_self_attack


card = PokemonCardDef(
    guid="c84f030c-d64c-5857-88ca-7b4d4f1c170a",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klink.Name",
    display_name="Klink",
    searchable_by=["Klink", "Basic", "Klink"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="BW5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=599,
    abilities=[
        Attack(
            title="Smash Turn",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=switch_self_attack(),
        ),
    ],
)