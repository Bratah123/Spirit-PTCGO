from spirit.game.data_utils import PokemonCardDef, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import no_special_conditions, playful_punch


card = PokemonCardDef(
    guid="b1daeb6b-9431-597d-9965-6569af3ac080",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Elekid.Name",
    display_name="Elekid",
    searchable_by=["Elekid", "Baby", "Elekid"],
    subtypes=["Baby"],
    collector_number=22,
    set_code="NEO1",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=239,
    abilities=[
        Ability(
            title="Playful Punch",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, do 20 damage to your opponent's Active Pok\u00e9mon. (Apply Weakness and Resistance.) Either way, this ends your turn. This power can't be used if Elekid is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            ends_turn=True,
            condition=no_special_conditions,
            effect=playful_punch,
        ),
    ],
)
