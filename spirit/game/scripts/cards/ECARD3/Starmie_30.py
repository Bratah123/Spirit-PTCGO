from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per, flip_or_nothing
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="eda20425-02e8-58fb-b599-37eee72adaa4",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Energy Burst",
            game_text="Flip a coin. If heads, this attack does 10 damage times the number of Energy attached to Starmie and the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="x",
            effect=flip_or_nothing(then=damage_per(
                lambda ctx: count_energy("self", cards=True)(ctx)
                + count_energy("defender", cards=True)(ctx),
                per=10,
            )),
        ),
        Attack(
            title="Star Back",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=attach_from_discard(
                predicate=is_basic_energy_card, count=1, target="choice",
                prompt="Choose a basic Energy card to attach",
            ),
        ),
    ],
)
