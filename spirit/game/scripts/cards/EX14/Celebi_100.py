from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import leaf_shade_energy_counters, time_travel_survive_flip

card = PokemonCardDef(
    guid="b5c35ce7-822a-5685-808b-472d9b8cd585",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name",
    display_name="Celebi ★",
    searchable_by=["Celebi \u2605", "Basic", "Star", "Celebi"],
    subtypes=["Basic", "Star"],
    collector_number=100,
    set_code="EX14",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Ability(
            title="Time Travel",
            game_text="If Celebi Star would be Knocked Out by damage from an opponent's attack, you may flip a coin. If heads, Celebi Star is not Knocked Out, discard all cards attached to Celebi Star, and put Celebi Star on the bottom of your deck.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=time_travel_survive_flip(),
            effect=None,
        ),
        Attack(
            title="Leaf Shade",
            game_text="Count the amount of Energy attached to Celebi Star. Put that many damage counters on 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
                        effect=leaf_shade_energy_counters(),
        ),
    ],
)