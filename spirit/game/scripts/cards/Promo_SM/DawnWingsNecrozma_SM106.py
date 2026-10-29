from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.smp import gulf_stream


card = PokemonCardDef(
    guid="5ebafa68-179c-5118-ae4c-5638a0f0df14",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DawnWingsNecrozma.Name",
    display_name="Dawn Wings Necrozma",
    searchable_by=["Dawn Wings Necrozma", "Basic", "Ultra Beast", "DawnWingsNecrozma"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=106,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=800,
    abilities=[
        Attack(
            title="Gulf Stream",
            game_text="If you have exactly 6 Prize cards remaining, this attack does 20 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator="+",
            effect=gulf_stream,
        ),
        Attack(
            title="Sword of Dawn",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=130,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)