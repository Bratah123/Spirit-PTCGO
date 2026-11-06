from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ecard import flames_of_rage, has_typed_basic_energy


card = PokemonCardDef(
    guid="c7635583-6923-511f-99ca-4fb9b4e313d7",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine", "Stage 1", "Arcanine"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=59,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
        Attack(
            title="Flames of Rage",
            game_text="Discard 2 Fire Energy cards attached to Arcanine in order to use this attack. This attack does 40 damage plus 10 more damage for each damage counter on Arcanine.",
            cost={PokemonTypes.FIRE: 2},
            damage=40,
            damage_operator="+",
            condition=has_typed_basic_energy(PokemonTypes.FIRE, 2),
            effect=flames_of_rage,
        ),
    ],
)
