from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="d3517913-f5fb-55bc-8a56-f6385addf39d",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianOverqwil.Name",
    display_name="Hisuian Overqwil",
    searchable_by=["Hisuian Overqwil", "Stage 1", "HisuianOverqwil"],
    subtypes=["Stage 1"],
    collector_number=90,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianQwilfish.Name",
    family_id=211,
    abilities=[
        Attack(
            title="Tormenting Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. During Pok\u00e9mon Checkup, put 5 damage counters on that Pok\u00e9mon instead of 1.",
            cost={},
            effect=condition_attack(SpecialConditions.POISONED, counters=5),
        ),
        Attack(
            title="Pinning",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)