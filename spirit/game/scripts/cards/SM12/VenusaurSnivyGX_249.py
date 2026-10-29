from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm12 import shining_vine, solar_plant_gx

card = PokemonCardDef(
    guid="b5d2c7e5-4639-5da0-92ce-b5cb9b204c59",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurSnivyGX.Name",
    display_name="Venusaur & Snivy-GX",
    searchable_by=["Venusaur & Snivy-GX", "Basic", "TAG TEAM", "GX", "VenusaurSnivyGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=249,
    set_code="SM12",
    rarity=Rarities.RareRainbow,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=3,
    abilities=[
        Ability(
            title="Shining Vine",
            game_text="Once during your turn, if this Pok\u00e9mon is your Active Pok\u00e9mon, when you attach a Grass Energy card from your hand to it, you may switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_ENERGY_ATTACHED,
            shared_once_per_turn="Shining Vine",
            effect=shining_vine,
        ),
        Attack(
            title="Forest Dump",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=160,
        ),
        Attack(
            title="Solar Plant-GX",
            game_text="This attack does 50 damage to each of your opponent's Pok\u00e9mon. If this Pok\u00e9mon has at least 2 extra Energy attached to it (in addition to this attack's cost), heal all damage from all of your Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=solar_plant_gx,
        ),
    ],
)