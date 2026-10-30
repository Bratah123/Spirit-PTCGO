from spirit.game.data_utils import PokemonCardDef, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import ditto_transform


card = PokemonCardDef(
    guid="f5cdf6e2-91f0-5ea6-9efd-965f95445100",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="BASE3",
    rarity=Rarities.RareHolo,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=132,
    abilities=[
        Ability(
            title="Transform",
            game_text="If Ditto is your Active Pok\u00e9mon, treat it as if it were the same card as the Defending Pok\u00e9mon, including type, Hit Points, Weakness, and so on, except Ditto can't evolve, always has this Pok\u00e9mon Power, and you may treat any Energy attached to Ditto as Energy of any type. Ditto isn't a copy of any other Pok\u00e9mon while Ditto is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=ditto_transform,
        ),
    ],
)
