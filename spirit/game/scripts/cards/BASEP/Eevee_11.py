from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import chain_reaction


card = PokemonCardDef(
    guid="4260b770-e1cc-58ae-9b8d-73915aba3cc3",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=133,
    abilities=[
        Ability(
            title="Chain Reaction",
            game_text="This power can only be used when a Pok\u00e9mon evolves. Search your deck for a card that evolves from Eevee and attach it to Eevee. This counts as evolving Eevee. Shuffle your deck afterward. This power can't be used if Eevee is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_POKEMON_EVOLVED,
            effect=chain_reaction,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
