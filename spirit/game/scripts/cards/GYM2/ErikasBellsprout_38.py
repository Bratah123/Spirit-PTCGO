from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ecard import soak_up, soak_up_condition


card = PokemonCardDef(
    guid="4a1550df-7ab3-5d0b-8ff8-e5bde8aa2f08",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasBellsprout.Name",
    display_name="Erika's Bellsprout",
    searchable_by=["Erika's Bellsprout", "Basic", "ErikasBellsprout"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=69,
    abilities=[
        Ability(
            title="Soak Up",
            game_text="Once during your turn (before your attack), you may take up to 2 Grass Energy cards attached to your other Pok\u00e9mon and attach them to Erika's Bellsprout. This power can't be used if Erika's Bellsprout is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=soak_up_condition,
            effect=soak_up,
        ),
        Attack(
            title="Stretch Vine",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon, and this attack does 10 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            effect=snipe_attack(10),
        ),
    ],
)
