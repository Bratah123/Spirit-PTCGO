from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.card_effects.ecard import miraculous_wind_passive


card = PokemonCardDef(
    guid="6c9bc5d2-8e77-5ea5-8e8a-614d318e39fc",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightDragonite.Name",
    display_name="Light Dragonite",
    searchable_by=["Light Dragonite", "Stage 2", "LightDragonite"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LightDragonair.Name",
    family_id=147,
    abilities=[
        Ability(
            title="Miraculous Wind",
            game_text="As long as Light Dragonite is your Active Pok\u00e9mon, each Special Energy card provides Colorless Energy instead of its usual type and its other effects stop working. This power stops working while Light Dragonite is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=miraculous_wind_passive,
        ),
        Attack(
            title="Light Wave",
            game_text="Prevent all effects of attacks, other than damage, done to Light Dragonite during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=protect_next_turn(effects_too=True),
        ),
    ],
)
