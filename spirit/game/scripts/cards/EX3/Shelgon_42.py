from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(
    guid="4a2c5a58-3fa3-5eeb-a025-49dffe7add2a",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    display_name="Shelgon",
    searchable_by=["Shelgon", "Stage 1", "Shelgon"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name",
    family_id=371,
    abilities=[
        Attack(
            title="Granite Head",
            game_text="Damage done to Shelgon by an opponent's attack is reduced by 10 (after applying Weakness and Resistance) during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=protect_next_turn(reduce=10),
        ),
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)