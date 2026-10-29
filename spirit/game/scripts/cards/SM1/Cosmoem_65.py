from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import switch_self_attack


card = PokemonCardDef(
    guid="1d11bd66-c16f-5ecb-bb20-b4b3351f3cd4",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    display_name="Cosmoem",
    searchable_by=["Cosmoem", "Stage 1", "Cosmoem"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="SM1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name",
    family_id=789,
    abilities=[
        Attack(
            title="Teleport",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=switch_self_attack(),
        ),
    ],
)