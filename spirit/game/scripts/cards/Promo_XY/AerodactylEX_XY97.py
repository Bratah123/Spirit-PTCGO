from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="b2b5018b-266f-5311-8c96-138ad5ce5865",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AerodactylEX.Name",
    display_name="Aerodactyl-EX",
    searchable_by=["Aerodactyl-EX", "Basic", "EX", "AerodactylEX"],
    subtypes=["Basic", "EX"],
    collector_number=97,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=142,
    abilities=[
        Attack(
            title="Rock Smash",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
        Attack(
            title="Land Crush",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)