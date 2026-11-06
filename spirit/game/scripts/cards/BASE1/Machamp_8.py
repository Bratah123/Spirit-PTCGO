from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import strikes_back


card = PokemonCardDef(
    guid="36acad07-0803-5a49-8f14-994f6eb1f47d",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="BASE1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Strikes Back",
            game_text="Whenever your opponent's attack damages Machamp (even if Machamp is Knocked Out), this power does 10 damage to the attacking Pok\u00e9mon. (Don't apply Weakness and Resistance.) This power can't be used if Machamp is Asleep, Confused, or Paralyzed when your opponent attacks.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=strikes_back,
        ),
        Attack(
            title="Seismic Toss",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
