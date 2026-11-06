from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ecard import ancient_wind, ancient_wind_condition


card = PokemonCardDef(
    guid="6bf39af7-4042-54a1-9432-908bf7205770",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactyl.Name",
    display_name="Aerodactyl",
    searchable_by=["Aerodactyl", "Stage 1", "Aerodactyl"],
    subtypes=["Stage 1"],
    collector_number=1,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=142,
    abilities=[
        Ability(
            title="Ancient Wind",
            game_text="Once during your turn (before your attack), if Aerodactyl is your Active Pok\u00e9mon, you may ignore all Pok\u00e9-Bodies until the end of your turn. This power can't be used if Aerodactyl is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=ancient_wind_condition,
            effect=ancient_wind,
        ),
        Attack(
            title="Rising Lunge",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)
