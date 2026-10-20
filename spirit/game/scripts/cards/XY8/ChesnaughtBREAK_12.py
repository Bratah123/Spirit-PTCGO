from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="e8f54453-bf41-5edd-84a8-6cea6f241f3f",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChesnaughtBREAK.Name",
    display_name="Chesnaught BREAK",
    searchable_by=["Chesnaught BREAK", "BREAK", "ChesnaughtBREAK"],
    subtypes=["BREAK"],
    collector_number=12,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chesnaught.Name",
    family_id=650,
    abilities=[
        Attack(
            title="Tough Hammer",
            game_text="This Pok\u00e9mon does 30 damage to itself. This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=snipe_attack(30, also_base=True, self_damage=30),
        ),
    ],
)