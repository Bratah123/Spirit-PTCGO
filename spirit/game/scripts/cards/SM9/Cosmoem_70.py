from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="829b2f1e-fa53-5801-82d2-5e5285085de9",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    display_name="Cosmoem",
    searchable_by=["Cosmoem", "Stage 1", "Cosmoem"],
    subtypes=["Stage 1"],
    collector_number=70,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name",
    family_id=789,
    abilities=[
        Attack(
            title="Nap",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=heal_attack(20),
        ),
    ],
)