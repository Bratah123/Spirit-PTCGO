from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import gather_fire, gather_fire_condition


card = PokemonCardDef(
    guid="3d6d1c6b-8a53-5778-92e3-a3251f0ebd3d",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    display_name="Charmander",
    searchable_by=["Charmander", "Basic", "Charmander"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="BASE5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=4,
    abilities=[
        Ability(
            title="Gather Fire",
            game_text="Once during your turn (before your attack), you may take 1 Fire Energy card attached to 1 of your other Pok\u00e9mon and attach it to Charmander. This power can't be used if Charmander is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=gather_fire_condition,
            effect=gather_fire,
        ),
        Attack(
            title="Fire Tail",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)
