from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on


card = PokemonCardDef(
    guid="bf93d9f8-d7dd-51f2-b2cb-2206a657d274",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MAlakazamEX.Name",
    display_name="M Alakazam-EX",
    searchable_by=["M Alakazam-EX", "MEGA", "EX", "MAlakazamEX"],
    subtypes=["MEGA", "EX"],
    collector_number=118,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlakazamEX.Name",
    family_id=65,
    abilities=[
        Attack(
            title="Zen Force",
            game_text="This attack does 30 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(damage_counters_on('defender'), 30, base=10),
        ),
    ],
)