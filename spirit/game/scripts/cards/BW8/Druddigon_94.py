from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="6e4ad10f-f89b-53b0-9e77-9897f8fb621f",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Druddigon.Name",
    display_name="Druddigon",
    searchable_by=["Druddigon", "Basic", "Team Plasma", "Druddigon"],
    subtypes=["Basic", "Team Plasma"],
    collector_number=94,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    family_id=621,
    abilities=[
        Attack(
            title="Guard Press",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=protect_next_turn(reduce=20),
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)