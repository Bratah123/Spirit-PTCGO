from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="5740da42-2ffe-5b54-abf5-da3cfd4c5e9d",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    display_name="Cosmoem",
    searchable_by=["Cosmoem", "Stage 1", "Cosmoem"],
    subtypes=["Stage 1"],
    collector_number=101,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name",
    family_id=789,
    abilities=[
        Attack(
            title="Stiffen",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 40 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=protect_next_turn(reduce=40),
        ),
    ],
)