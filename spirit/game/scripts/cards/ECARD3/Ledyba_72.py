from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="52858abf-ac9a-5ab6-bfb3-a1f90ca23621",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name",
    display_name="Ledyba",
    searchable_by=["Ledyba", "Basic", "Ledyba"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=165,
    abilities=[
        Attack(
            title="Teary Eyes",
            game_text="During your opponent's next turn, any damage done to Ledyba by attacks is reduced by 20.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=protect_next_turn(reduce=20),
        ),
        Attack(
            title="Quick Turn",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=10),
        ),
    ],
)
