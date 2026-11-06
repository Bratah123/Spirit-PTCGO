from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import MirrorCoatPassive, return_attack


card = PokemonCardDef(
    guid="4818bdcc-31ef-56f5-8877-c3d9a58b5de9",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    display_name="Wobbuffet",
    searchable_by=["Wobbuffet", "Basic", "Wobbuffet"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=202,
    abilities=[
        Ability(
            title="Mirror Coat",
            game_text="If Wobbuffet becomes Poisoned or Burned by the Defending Pok\u00e9mon's attack during your opponent's turn, the Defending Pok\u00e9mon becomes affected by the same Special Condition.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=MirrorCoatPassive(),
        ),
        Attack(
            title="Return Attack",
            game_text="Flip 2 coins. If either is heads, this attack does 10 damage times the number of damage counters on Wobbuffet.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=return_attack,
        ),
    ],
)
