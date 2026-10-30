from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import burn_up, healing_fire


card = PokemonCardDef(
    guid="4021253d-49c8-5b14-ba69-1e66afff701c",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesNinetales.Name",
    display_name="Blaine's Ninetales",
    searchable_by=["Blaine's Ninetales", "Stage 1", "BlainesNinetales"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="GYM2",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesVulpix.Name",
    family_id=37,
    abilities=[
        Ability(
            title="Healing Fire",
            game_text="Whenever you attach a Fire Energy card from your hand to Blaine's Ninetales, remove 1 damage counter from it, if it has any. This power stops working when Blaine's Ninetales is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=healing_fire,
        ),
        Attack(
            title="Burn Up",
            game_text="Flip a coin. If tails, discard all Fire Energy cards attached to Blaine's Ninetales.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            effect=burn_up,
        ),
    ],
)
