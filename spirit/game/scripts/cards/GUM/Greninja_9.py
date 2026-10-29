from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import flip_prevent_damage_passive
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="82c71c13-dd70-5e6b-bbca-a0a2d70abd4a",
    key="GUM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greninja.Name",
    display_name="Greninja",
    searchable_by=["Greninja", "Stage 2", "Greninja"],
    subtypes=["Stage 2"],
    collector_number=9,
    set_code="GUM",
    rarity=Rarities.RareUltra,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=658,
    abilities=[
        Ability(
            title="Evasion Jutsu",
            game_text="If any damage is done to this Pok\u00e9mon by attacks, flip a coin. If heads, prevent that damage.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=flip_prevent_damage_passive("Evasion Jutsu"),
        ),
        Attack(
            title="Furious Shurikens",
            game_text="This attack does 50 damage to 2 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2},
            effect=snipe_attack(50, pool='any', count=2),
        ),
    ],
)