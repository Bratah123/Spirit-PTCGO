from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ecard import foresight


card = PokemonCardDef(
    guid="67e2ab43-f987-5669-a335-0a48088a99ef",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name",
    display_name="Hypno",
    searchable_by=["Hypno", "Stage 1", "Hypno"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="BASE3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=97,
    abilities=[
        Attack(
            title="Prophecy",
            game_text="Look at up to 3 cards from the top of either player's deck and rearrange them as you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=foresight,
        ),
        Attack(
            title="Dark Mind",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them and this attack does 10 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=30,
            effect=snipe_attack(10, also_base=True),
        ),
    ],
)
