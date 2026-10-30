"""DP2 Mysterious Treasures — wired.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="975871fd-9356-5564-9baf-7a0171bcc393",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cranidos.Name",
    display_name="Cranidos",
    searchable_by=["Cranidos", "Stage 1", "Cranidos"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SkullFossil.Name",
    family_id=408,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Steamroll",
            game_text="Does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=snipe_attack(20),
        ),
    ],
)