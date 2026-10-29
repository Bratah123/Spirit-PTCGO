from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.card_effects.sm12 import cold_snap, cold_snap_condition


card = PokemonCardDef(
    guid="f10f8ca1-5ae8-5bf9-94ea-5f579e3ff1cc",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Walrein.Name",
    display_name="Walrein",
    searchable_by=["Walrein", "Stage 2", "Walrein"],
    subtypes=["Stage 2"],
    collector_number=52,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name",
    family_id=363,
    abilities=[
        Attack(
            title="Cold Snap",
            game_text="Your opponent can't play any Trainer cards from their hand during their next turn. If 1 of your Pok\u00e9mon used Cold Snap during your last turn, this attack can't be used.",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            condition=cold_snap_condition,
            effect=cold_snap,
        ),
        Attack(
            title="Blizzard",
            game_text="This attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=spread_damage(10, also_base=True),
        ),
    ],
)