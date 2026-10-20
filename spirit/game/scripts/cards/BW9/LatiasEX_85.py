from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, ignore_effects_attack


card = PokemonCardDef(
    guid="77e8c458-a2ad-59c0-92d6-78f59415ed08",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LatiasEX.Name",
    display_name="Latias-EX",
    searchable_by=["Latias-EX", "Basic", "EX", "LatiasEX"],
    subtypes=["Basic", "EX"],
    collector_number=85,
    set_code="BW9",
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    family_id=380,
    abilities=[
        Ability(
            title="Bright Down",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon by your opponent's Pok\u00e9mon with Abilities.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Barrier Break",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=ignore_effects_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)