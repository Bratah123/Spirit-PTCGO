from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage


card = PokemonCardDef(
    guid="01d2903b-0b11-5505-bdc1-8dc2e965c4bf",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MAerodactylEX.Name",
    display_name="M Aerodactyl-EX",
    searchable_by=["M Aerodactyl-EX", "MEGA", "EX", "MAerodactylEX"],
    subtypes=["MEGA", "EX"],
    collector_number=98,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AerodactylEX.Name",
    family_id=142,
    abilities=[
        Attack(
            title="Rock Drill Dive",
            game_text="This attack does 10 damage to each Benched Pok\u00e9mon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=spread_damage(10, side='both', also_base=True),
        ),
    ],
)