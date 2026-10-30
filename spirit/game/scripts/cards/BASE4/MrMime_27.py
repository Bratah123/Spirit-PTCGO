from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per
from spirit.game.card_effects.ecard import invisible_wall


card = PokemonCardDef(
    guid="25104cb1-82df-5617-82d2-bfe6a6ab53af",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="BASE4",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=122,
    abilities=[
        Ability(
            title="Invisible Wall",
            game_text="Whenever an attack (including your own) does 30 or more damage to Mr. Mime (after applying Weakness and Resistance), prevent that damage. (Any other effects of attacks still happen.) This power stops working while Mr. Mime is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=invisible_wall,
        ),
        Attack(
            title="Meditate",
            game_text="Does 10 damage plus 10 more damage for each damage counter on the Defending Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), 10, base=10),
        ),
    ],
)
