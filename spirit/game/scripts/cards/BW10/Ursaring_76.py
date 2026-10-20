from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import boost_own_next_turn


card = PokemonCardDef(
    guid="4fcea7cf-69a2-5819-baa6-90c9c16f257c",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ursaring.Name",
    display_name="Ursaring",
    searchable_by=["Ursaring", "Stage 1", "Team Plasma", "Ursaring"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=76,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    family_id=216,
    abilities=[
        Attack(
            title="Adrenalash",
            game_text="During your next turn, each of this Pok\u00e9mon's attacks does 50 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=boost_own_next_turn(50),
        ),
        Attack(
            title="Strength",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
        ),
    ],
)