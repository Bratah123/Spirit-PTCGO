from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, count_energy

card = PokemonCardDef(
    guid="e5de5d4a-5604-5394-a129-80c522af8ded",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianOverqwil.Name",
    display_name="Hisuian Overqwil",
    searchable_by=["Hisuian Overqwil", "Stage 1", "HisuianOverqwil"],
    subtypes=["Stage 1"],
    collector_number=91,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianQwilfish.Name",
    family_id=211,
    abilities=[
        Attack(
            title="Dirty Press",
            game_text="If you have at least 3 Darkness Energy in play, this attack does 90 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(
                lambda ctx: count_energy("mine", energy_type=PokemonTypes.DARKNESS)(ctx) >= 3,
                90, base=30),
        ),
        Attack(
            title="Pierce",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)