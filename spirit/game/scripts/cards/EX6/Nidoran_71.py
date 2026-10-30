from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ex import call_for_family_nidoran


card = PokemonCardDef(
    guid="bcdbba5a-44a1-56ee-b568-24dc781d444f",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name",
    display_name="Nidoran ♂",
    searchable_by=["Nidoran \u2642", "Basic", "Nidoran"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="EX6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=32,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Nidoran \u2640 or Nidoran \u2642 card and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=call_for_family_nidoran(),
        ),
        Attack(
            title="Double Stab",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=10),
        ),
    ],
)