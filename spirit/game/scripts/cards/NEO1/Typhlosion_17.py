from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import fire_recharge, fire_recharge_condition, flame_burst


card = PokemonCardDef(
    guid="a8f9fe61-44be-5d0b-9117-29e20c57cc6e",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name",
    display_name="Typhlosion",
    searchable_by=["Typhlosion", "Stage 2", "Typhlosion"],
    subtypes=["Stage 2"],
    collector_number=17,
    set_code="NEO1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    family_id=155,
    abilities=[
        Ability(
            title="Fire Recharge",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, attach a Fire Energy card from your discard pile to 1 of your Fire Pok\u00e9mon. This power can't be used if Typhlosion is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=fire_recharge_condition,
            effect=fire_recharge,
        ),
        Attack(
            title="Flame Burst",
            game_text="Flip a coin. If heads, this attack does 60 damage plus 20 more damage and does 20 damage to Typhlosion. If tails, this attack does 60 damage.",
            cost={PokemonTypes.FIRE: 4},
            damage=60,
            damage_operator="+",
            effect=flame_burst,
        ),
    ],
)
