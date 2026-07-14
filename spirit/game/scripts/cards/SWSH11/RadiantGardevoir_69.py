from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.passives_common import takes_less_passive

card = PokemonCardDef(
    guid="bb21c8f8-7fe3-58e6-8e3f-e062f9f2a50d",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantGardevoir.Name",
    display_name="Radiant Gardevoir",
    searchable_by=["Radiant Gardevoir", "Basic", "Radiant", "RadiantGardevoir"],
    subtypes=["Basic", "Radiant"],
    collector_number=69,
    set_code="SWSH11",
    rarity=Rarities.RareRadiant,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=282,
    abilities=[
        Ability(
            title="Loving Veil",
            game_text="All of your Pok\u00e9mon take 20 less damage from attacks from your opponent's Pok\u00e9mon V (after applying Weakness and Resistance).",
            passive=takes_less_passive(
                20, protects="team",
                attacker_pred=lambda p: is_pokemon_v(p.archetype_id),
            ),
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 20 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 20, base=70),
        ),
    ],
)