from spirit.game.card_effects.pokemon import fusion_strike_system, fusion_strike_system_condition
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cb9ff20d-68e5-541f-a08d-1d155c7e6605",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GenesectV.Name",
    display_name="Genesect V",
    searchable_by=["Genesect V", "Basic", "V", "Fusion Strike", "GenesectV"],
    subtypes=["Basic", "V", "Fusion Strike"],
    collector_number=255,
    set_code="SWSH8",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=649,
    abilities=[
        Ability(
            title="Fusion Strike System",
            game_text="Once during your turn, you may draw cards until you have as many cards in your hand as you have Fusion Strike Pok\u00e9mon in play.",
            activation=Activations.ONCE_PER_TURN,
            condition=fusion_strike_system_condition,
            effect=fusion_strike_system,
        ),
        Attack(
            title="Techno Blast",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=210,
            locks_next_turn=True,
        ),
    ],
)