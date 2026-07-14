from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.passives import Passive
from spirit.game.card_effects.attacks_common import lock_all_attacks


class CrisisMusclesPassive(Passive):
    def max_hp_bonus(self, pokemon, carrier):
        if pokemon is not carrier:
            return 0
        root = pokemon
        while root.parent is not None:
            root = root.parent
        for child in root.children:
            if getattr(child, "owning_player_id", None) and \
                    child.owning_player_id != pokemon.owning_player_id:
                for sub in child.children:
                    if sub.get_attribute(AttrID.NAME) == "prizePile" and \
                            len(sub.children) <= 3:
                        return 150
        return 0


async def strong_arm_lariat(ctx):
    """You may do 100 more damage; if you do, this Pokémon can't attack next turn."""
    if await ctx.ask_yes_no(
        "Do 100 more damage? If you do, this Pokémon can't attack during "
        "your next turn."
    ):
        await ctx.deal_damage(200)
        lock_all_attacks(ctx, ctx.attacker)
    else:
        await ctx.deal_damage(100)


card = PokemonCardDef(
    guid="f300a416-8ca5-5ebb-b0b0-e2f31615d632",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=88,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Ability(
            title="Crisis Muscles",
            game_text="If your opponent has 3 or fewer Prize cards remaining, this Pok\u00e9mon gets +150 HP.",
            passive=CrisisMusclesPassive(),
        ),
        Attack(
            title="Strong-Arm Lariat",
            game_text="You may do 100 more damage. If you do, during your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=100,
            damage_operator="+",
            effect=strong_arm_lariat,
        ),
    ],
)