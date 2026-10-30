from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.ex import safeguard_ex_passive


card = PokemonCardDef(
    guid="092603b3-1d9b-5b38-bab5-c53e88b53725",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    display_name="Wobbuffet",
    searchable_by=["Wobbuffet", "Basic", "Wobbuffet"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="EX2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=202,
    abilities=[
        Ability(
            title="Safeguard",
            game_text="Prevent all effects of attacks, including damage, done to Wobbuffet by your opponent's Pok\u00e9mon-ex.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=safeguard_ex_passive(),
        ),
        Attack(
            title="Flip Over",
            game_text="Wobbuffet does 10 damage to itself, and don't apply Weakness and Resistance to this damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=recoil_attack(10),
        ),
    ],
)
