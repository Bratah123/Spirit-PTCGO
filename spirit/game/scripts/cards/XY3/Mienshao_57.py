from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import remove_self_from_play


card = PokemonCardDef(
    guid="6ca8ba41-53c9-5902-8960-af7c3d822fdc",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mienshao.Name",
    display_name="Mienshao",
    searchable_by=["Mienshao", "Stage 1", "Mienshao"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mienfoo.Name",
    family_id=619,
    abilities=[
        Attack(
            title="Aero Turn",
            game_text="Return this Pok\u00e9mon and all cards attached to it to your hand.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=remove_self_from_play('hand'),
        ),
        Attack(
            title="High Jump Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)