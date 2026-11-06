from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import entei_bolt, protective_flame


card = PokemonCardDef(
    guid="6fffe00a-c089-5367-b118-dfaaa744ad49",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name",
    display_name="Entei",
    searchable_by=["Entei", "Basic", "Entei"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Ability(
            title="Bolt",
            game_text="Whenever your opponent's attack damages Entei, unless that attack Knocks Out Entei, flip a coin. If heads, shuffle Entei and all cards attached to it into your deck. This power can't be used if Entei is already Asleep, Confused, or Paralyzed when it is damaged.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=entei_bolt,
        ),
        Attack(
            title="Protective Flame",
            game_text="During your opponent's next turn, prevent all effects of attacks, including damage, done to your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 3},
            damage=50,
            effect=protective_flame,
        ),
    ],
)
