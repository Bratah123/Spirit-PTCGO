from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import team_damage_boost_passive


card = PokemonCardDef(
    guid="7da46a72-fa1e-52a2-9897-54f00e28771c",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactyl.Name",
    display_name="Aerodactyl",
    searchable_by=["Aerodactyl", "Restored", "Aerodactyl"],
    subtypes=["Restored"],
    collector_number=53,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.RESTORED,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.OldAmberAerodactyl.Name",
    family_id=142,
    abilities=[
        Ability(
            title="Ancient Scream",
            game_text="Your Pok\u00e9mon's attacks do 10 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=team_damage_boost_passive(10),
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)